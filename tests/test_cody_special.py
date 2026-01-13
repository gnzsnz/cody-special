"""Tests for cody-special package."""
import pytest
from math import isclose, isinf, isnan

from cody_special import (
    erf_cody, erfc_cody, erfcx_cody,
    norm_pdf, norm_cdf, inverse_norm_cdf
)


class TestErfCody:
    """Tests for error functions."""

    def test_erf_zero(self):
        assert erf_cody(0.0) == 0.0

    def test_erf_positive(self):
        # erf(1) ~ 0.8427007929497149
        assert isclose(erf_cody(1.0), 0.8427007929497149, rel_tol=1e-15)

    def test_erf_negative(self):
        # erf is odd function
        assert isclose(erf_cody(-1.0), -erf_cody(1.0), rel_tol=1e-15)

    def test_erfc_zero(self):
        assert erfc_cody(0.0) == 1.0

    def test_erfc_large(self):
        # erfc(x) -> 0 as x -> inf
        assert erfc_cody(10.0) < 1e-40

    def test_erfcx_positive(self):
        # erfcx(x) = exp(x^2) * erfc(x)
        # erfcx(1) ~ 0.42758357615580700
        assert isclose(erfcx_cody(1.0), 0.42758357615580700, rel_tol=1e-14)


class TestNormalDistribution:
    """Tests for normal distribution functions."""

    def test_norm_pdf_zero(self):
        # phi(0) = 1/sqrt(2*pi) ~ 0.3989422804014327
        assert isclose(norm_pdf(0.0), 0.3989422804014327, rel_tol=1e-15)

    def test_norm_pdf_symmetric(self):
        assert isclose(norm_pdf(1.0), norm_pdf(-1.0), rel_tol=1e-15)

    def test_norm_cdf_zero(self):
        # Phi(0) = 0.5
        assert isclose(norm_cdf(0.0), 0.5, rel_tol=1e-15)

    def test_norm_cdf_large_positive(self):
        # Phi(x) -> 1 as x -> inf
        assert isclose(norm_cdf(10.0), 1.0, rel_tol=1e-15)

    def test_norm_cdf_large_negative(self):
        # Phi(x) -> 0 as x -> -inf
        assert norm_cdf(-10.0) < 1e-20

    def test_inverse_norm_cdf_half(self):
        # Phi^{-1}(0.5) = 0
        assert isclose(inverse_norm_cdf(0.5), 0.0, abs_tol=1e-15)

    def test_inverse_norm_cdf_round_trip(self):
        # Phi^{-1}(Phi(x)) = x
        for x in [-2.0, -1.0, 0.0, 1.0, 2.0]:
            assert isclose(inverse_norm_cdf(norm_cdf(x)), x, rel_tol=1e-14)

    def test_norm_cdf_round_trip(self):
        # Phi(Phi^{-1}(p)) = p
        for p in [0.1, 0.25, 0.5, 0.75, 0.9]:
            assert isclose(norm_cdf(inverse_norm_cdf(p)), p, rel_tol=1e-14)
