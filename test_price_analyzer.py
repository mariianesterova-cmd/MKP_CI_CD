import pytest
import os
from datetime import datetime, timedelta
from price_analyzer import filter_last_month, calculate_price_change


@pytest.fixture
def sample_data():
    now = datetime.now()
    return [
        ("Apple", now - timedelta(days=10), 100.0),
        ("Apple", now - timedelta(days=5), 120.0),
        ("Banana", now - timedelta(days=5), 50.0),
        ("Apple", now - timedelta(days=40), 80.0), 
    ]

@pytest.mark.parametrize("product, expected_count", [
    ("Apple", 2),
    ("Banana", 1),
    ("Orange", 0),
])
def test_filter_last_month(sample_data, product, expected_count):
    result = filter_last_month(sample_data, product)
    assert len(result) == expected_count

def test_calculate_price_change():
    data = [
        (datetime(2026, 1, 1), 100.0),
        (datetime(2026, 1, 15), 150.0)
    ]
    assert calculate_price_change(data) == 50.0