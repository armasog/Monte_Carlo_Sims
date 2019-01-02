from numpy import random, mean
import matplotlib.pyplot as plt
'''
Problem:

You are considering leasing a machine for some manufacturing process. The one-year lease costs you $400,000, and you cannot cancel early. You wonder whether the annual production level and the savings in maintenance, labor, and raw materials are high enough to justify leasing the machine.

From your human experts, you got the following ranges of variables (note that all ranges have 90% confidence interval and values are normally distributed):

maintenance savings: 10−20 USD per unit
labor savings: -2–8 USD per unit
raw material savings: 3−9 USD per unit
production level: 15,000–35,000 units per year
annual lease: $400000
the annual savings = (maintenance savings + labor savings + raw material savings) * production level

'''

def monte_carlo_machine(iterations=1000000, plot=True):
    _90_confidence_interval = 3.29
    savings_per_trial = []
    trials_losing_money = 0
    for i in range(iterations+1):
        maintenance = random.normal(loc=(20+10)/2, scale=(20-10) / _90_confidence_interval)
        labor = random.normal(loc=(8+-2)/2, scale=(8--2) / _90_confidence_interval)
        raw_material = random.normal(loc=(9+3)/2, scale=(9-3) / _90_confidence_interval)
        production = random.normal(loc=(35000+15000)/2, scale=(35000-15000) / _90_confidence_interval)
        savings_per_trial.append((maintenance+labor+raw_material) * production)
    for j in savings_per_trial: # Count the number of trials where cost of lease exceeds savings
        if j < 400000:
            trials_losing_money += 1
    if plot:
        plt.hist(savings_per_trial, bins = 100)
        plt.axvline(x = 400000, c = 'r')
        plt.show()
    return float(trials_losing_money/iterations)

monte_carlo_machine()
