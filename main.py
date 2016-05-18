from evaluate import evaluate

__author__ = "Sushant Raikar"
__email__ = "sushantraikar123@yahoo.com"

data = '[{"state": {"cities": ["Mumbai", "Pune", "Nagpur", "Bhusaval", "Jalgaon"], "name": "Maharashtra"}}, {"state": {"cities": ["Bangalore", "Hubli"], "name": "Karnataka"}}, {"state": {"states": ["Raipur", "Durg"], "name": "Chhattisgarh"}}]'
a = evaluate(data)
