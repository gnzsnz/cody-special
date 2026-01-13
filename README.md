# cody-special

High-precision error functions and normal distribution implementations based on W.J. Cody's rational Chebyshev approximations.

## Installation

```bash
pip install cody-special
```

## Usage

```python
from cody_special import erf_cody, erfc_cody, erfcx_cody
from cody_special import norm_pdf, norm_cdf, inverse_norm_cdf

# Error functions
erf_cody(1.0)      # ~ 0.8427
erfc_cody(1.0)     # ~ 0.1573
erfcx_cody(1.0)    # ~ 0.4276

# Normal distribution
norm_pdf(0.0)           # ~ 0.3989 (standard normal PDF)
norm_cdf(0.0)           # = 0.5 (standard normal CDF)
inverse_norm_cdf(0.5)   # = 0.0 (inverse CDF / quantile function)
```

## References

- W.J. Cody, "Rational Chebyshev approximations for the error function", Math. Comp., 1969, pp. 631-638.
- Peter Jaeckel, "Let's Be Rational", www.jaeckel.org

## License

MIT License. Original algorithm by W.J. Cody. Python implementation derived from Peter Jaeckel's LetsBeRational.
