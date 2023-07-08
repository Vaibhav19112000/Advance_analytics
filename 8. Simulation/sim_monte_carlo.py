import pandas as pd 
import numpy as np 

rnd = np.random.rand(10)
rnd
x = np.array([0,1,2,3,4,5,6])
probs = np.array([0.3,0.2,0.2,0.08,0.16,0.02,0.04])
cums = np.cumsum(probs)

exp_x = np.dot(x, probs)
print("Expected Value =", exp_x)

# for finding any value
d = 0.502103165001252
finding = d > cums
i_finding = np.sum(finding)
x[i_finding]

rnd = np.random.rand(100)
rnd
sim = []
for d in rnd:
    finding = d > cums
    i_finding = np.sum(finding)
    sim.append(x[i_finding])
    
print("Mean of Simulated =", np.mean(sim))

############ Prob 2 ######################
x = np.array([0,5,10,15,20,25])
probs = np.array([0.04,0.22,0.16,0.42,0.1,0.06])
cums = np.cumsum(probs)

exp_x = np.dot(x, probs)
print("Expected Value =", exp_x)

rnd = np.random.rand(100)
sim = []
for d in rnd:
    finding = d > cums
    i_finding = np.sum(finding)
    sim.append(x[i_finding])
    
print("Mean of Simulated =", np.mean(sim))

######## Sick Drivers #########################
x = np.array([0,1,2,3,4,5])
probs = np.array([0.3,0.2,0.15,0.1,0.13,0.12])
cums = np.cumsum(probs)

exp_x = np.dot(x, probs)
print("Expected Value =", exp_x)

rnd = np.random.rand(100)
sim = []
for d in rnd:
    finding = d > cums
    i_finding = np.sum(finding)
    sim.append(x[i_finding])

reserved = 2
sim = np.array(sim)
print("No. of Days buses require cancellation =",np.sum(sim > reserved))

############# Suppy - Demand ##########################
supply = np.array([10, 20, 30, 40, 50])
supp_prob = np.array([40,50,190,150,70])/500 
cums_supp = np.cumsum(supp_prob)

demand = np.array([10, 20, 30, 40, 50])
dem_prob = np.array([50,110,200,100,40])/500
cums_demand = np.cumsum(dem_prob)

rnd = np.random.rand(30)
sim_demand = []
for d in rnd:
    finding = d > cums_demand
    i_finding = np.sum(finding)
    sim_demand.append(demand[i_finding])

rnd = np.random.rand(30)
sim_supply = []
for d in rnd:
    finding = d > cums_supp
    i_finding = np.sum(finding)
    sim_supply.append(supply[i_finding])

sim_df = pd.DataFrame({'sim_supply':sim_supply,
                       'sim_demand':sim_demand})
sim_df['sold'] = np.minimum(sim_supply, sim_demand)

sim_supply = np.array(sim_supply)
sim_demand = np.array(sim_demand)
sim_df['perished'] = np.where(sim_supply>sim_demand,
                              sim_supply-sim_demand ,
                              0)
sim_df['profit'] = sim_df['sold']*10
sim_df['loss'] = sim_df['perished']*8
sim_df['net_profit'] = sim_df['profit'] - sim_df['loss']
