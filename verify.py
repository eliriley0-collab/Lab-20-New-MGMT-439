"""Executable course checks. Synthetic CSV data tests parsing, never market evidence."""
import copy
import io
import math
import portfolio as p


def run():
    baseline = p.search(p.RETURNS, p.VOLATILITIES, p.CORRELATIONS, .065, p.RESERVE_ELIGIBLE, .03)
    lower = p.RETURNS.copy()
    lower[-1] = .07
    stress = p.search(lower, p.VOLATILITIES, p.CORRELATIONS, .065, p.RESERVE_ELIGIBLE, .03)
    changed = copy.deepcopy(p.CORRELATIONS)
    changed[2][3] = changed[3][2] = .5
    correlation = p.search(p.RETURNS, p.VOLATILITIES, changed, .065, p.RESERVE_ELIGIBLE, .03)
    for label, result, weights, ret, risk in [
        ('As loaded', baseline, [0, .2, .25, .55], '6.51', '9.44'),
        ('Equity 7%', stress, [0, .1, .1, .8], '6.53', '12.94'),
        ('IG/equity correlation .50', correlation, [0, .4, 0, .6], '6.52', '9.73'),
    ]:
        assert result['weights'] == weights, result
        assert f'{result["return_estimate"] * 100:.2f}' == ret
        assert f'{result["volatility"] * 100:.2f}' == risk
        print(label, result)
    assert math.isclose(max(abs(a-b) for a,b in zip(baseline['weights'], stress['weights'])) * 100, 25)
    assert p.search(p.RETURNS, p.VOLATILITIES, p.CORRELATIONS, .09, p.RESERVE_ELIGIBLE, .03) is None
    for bad in (1.3, .4):
        invalid = copy.deepcopy(p.CORRELATIONS)
        invalid[2][3] = bad
        try:
            p.covariance_matrix(p.VOLATILITIES, invalid)
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid correlation accepted')
    rows = ['Date,TEST_A,TEST_B,TEST_C']
    for t in range(61):
        rows.append(f'{2020+t//12}-{t%12+1:02d}-01,' + ','.join(str(100*(1+r)**t) for r in (.001,.002,.003)))
    csv = '\n'.join(rows)
    full = p.estimate_csv(io.StringIO(csv))
    recent = p.estimate_csv(io.StringIO(csv), True)
    assert full[-1] == 60 and recent[-1] == 36
    assert all(math.isclose(a,b,abs_tol=1e-12) for a,b in zip(full[1],[.012,.024,.036]))
    print('PASS: three Meridian runs, 25-point shift, infeasibility, bad correlations, and synthetic CSV annualization/window.')


if __name__ == '__main__':
    run()
