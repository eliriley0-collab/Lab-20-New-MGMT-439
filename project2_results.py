"""Reproduce Project 2 results with the student's target and reserve rule."""
import json
from pathlib import Path
import portfolio as engine

ROOT = Path(__file__).resolve().parent


def results():
    output = {'objective': .05, 'reserve_minimum': .05, 'reserve_eligible': ['BIL']}
    for label, recent in [('all_months', False), ('last_36', True)]:
        with (ROOT / 'prices.csv').open() as source:
            names, returns, vols, correlations, count = engine.estimate_csv(source, recent)
        answer = engine.search(returns, vols, correlations, .05, [n == 'BIL' for n in names], .05)
        output[label] = dict(assets=names, monthly_returns=count, annual_return_estimates=returns,
                             annual_volatility_estimates=vols, correlations=correlations, answer=answer)
    full, recent = output['all_months']['answer'], output['last_36']['answer']
    output['largest_weight_change_points'] = (max(abs(a-b) for a,b in zip(full['weights'], recent['weights'])) * 100
                                              if full and recent else None)
    inputs = output['all_months']
    stressed_returns = inputs['annual_return_estimates'].copy()
    stressed_returns[inputs['assets'].index('BIL')] -= .01
    output['ai_stress_bil_minus_one_point'] = engine.search(
        stressed_returns, inputs['annual_volatility_estimates'], inputs['correlations'],
        .05, [n == 'BIL' for n in inputs['assets']], .05)
    return output


if __name__ == '__main__':
    output = results()
    (ROOT / 'project2_results.json').write_text(json.dumps(output, indent=2) + '\n')
    for label in ['all_months', 'last_36']:
        print(label, output[label]['answer'])
        print('Annual return estimates:', output[label]['annual_return_estimates'])
    print('Largest change (points):', output['largest_weight_change_points'])
