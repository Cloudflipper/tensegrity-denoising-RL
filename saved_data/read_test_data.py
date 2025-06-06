import numpy as np
import matplotlib.pyplot as plt

reward_forward_data = np.load('reward_forward_data.npy')
reward_ctrl_data = np.load('reward_ctrl_data.npy')
action_data = np.load('action_data.npy')
tendon_data = np.load('tendon_data.npy')
oript_data = np.load('oript_data.npy')
iniyaw_data = np.load('iniyaw_data.npy')
<<<<<<< HEAD
waypt_data = np.load('waypt_data.npy', allow_pickle=True)
x_pos_data = np.load('x_pos_data.npy')
y_pos_data = np.load('y_pos_data.npy')

predicted_friction_data = np.load('predicted_friction_data.npy')
predicted_damping_c_data = np.load('predicted_damping_c_data.npy')
predicted_stiffness_c_data = np.load('predicted_stiffness_c_data.npy')
friction_data = np.load('friction_data.npy')
damping_c_data = np.load('damping_c_data.npy')
stiffness_c_data = np.load('stiffness_c_data.npy')

obs_posi_data = np.load('obs_posi_data.npy')
gt_posi_data = np.load('gt_posi_data.npy')
#predicted_posi_data = np.load('predicted_posi_data.npy')

=======
x_pos_data = np.load('x_pos_data.npy')
y_pos_data = np.load('y_pos_data.npy')
>>>>>>> origin/dev-incorporate-transformer

action_subdata = action_data
plt.figure(figsize=(12, 4))
plt.subplot(611)
plt.plot(action_subdata[:,0], marker='.', linestyle='-')
plt.ylabel('action subdata 0')
plt.grid()
plt.subplot(612)
plt.plot(action_subdata[:,1], marker='.', linestyle='-')
plt.ylabel('action subdata 1')
plt.grid()
plt.subplot(613)
plt.plot(action_subdata[:,2], marker='.', linestyle='-')
plt.ylabel('action subdata 2')
plt.grid()
plt.subplot(614)
plt.plot(action_subdata[:,3], marker='.', linestyle='-')
plt.ylabel('action subdata 3')
plt.grid()
plt.subplot(615)
plt.plot(action_subdata[:,4], marker='.', linestyle='-')
plt.ylabel('action subdata 4')
plt.grid()
plt.subplot(616)
plt.plot(action_subdata[:,5], marker='.', linestyle='-')
plt.ylabel('action subdata 5')
plt.grid()

plt.tight_layout()
plt.savefig('saved_plots/action_data_subplots.png')
plt.close()

active_tendon_subdata = tendon_data[:,:6] - 0.15
plt.figure(figsize=(12, 4))
plt.subplot(611)
plt.plot(active_tendon_subdata[:,0], marker='.', linestyle='-')
plt.ylabel('active tendon subdata 0')
plt.grid()
plt.subplot(612)
plt.plot(active_tendon_subdata[:,1], marker='.', linestyle='-')
plt.ylabel('active tendon subdata 1')
plt.grid()
plt.subplot(613)
plt.plot(active_tendon_subdata[:,2], marker='.', linestyle='-')
plt.ylabel('active tendon subdata 2')
plt.grid()
plt.subplot(614)
plt.plot(active_tendon_subdata[:,3], marker='.', linestyle='-')
plt.ylabel('active tendon subdata 3')
plt.grid()
plt.subplot(615)
plt.plot(active_tendon_subdata[:,4], marker='.', linestyle='-')
plt.ylabel('actiactive tendonon subdata 4')
plt.grid()
plt.subplot(616)
plt.plot(active_tendon_subdata[:,5], marker='.', linestyle='-')
plt.ylabel('active tendon subdata 5')
plt.grid()

<<<<<<< HEAD
plt.tight_layout()
plt.savefig('saved_plots/tendon_data_subplots.png')
plt.close()


plt.figure(figsize=(5, 5))
=======
plt.figure(figsize=(12, 8))
>>>>>>> origin/dev-incorporate-transformer
vector_length = 1
iniyaw = iniyaw_data[0]
vec_endpt = oript_data + vector_length * np.array([np.cos(iniyaw), np.sin(iniyaw)])
plt.plot([oript_data[0], vec_endpt[0]], [oript_data[1], vec_endpt[1]], 'r-', label='forward direction')
plt.scatter([oript_data[0]], [oript_data[1]], color='blue', label='original point')
<<<<<<< HEAD
#plt.scatter([waypt_data[0]], [waypt_data[1]], color='green', label='waypoint')
=======
>>>>>>> origin/dev-incorporate-transformer
plt.plot(x_pos_data, y_pos_data, marker='.', linestyle='-')
plt.axis('equal')
plt.title('x-y position')
plt.xlabel('x')
plt.ylabel('y')
<<<<<<< HEAD
plt.legend()
plt.grid()
plt.savefig('saved_plots/xy_position_plot.png')
plt.close()


plt.figure(figsize=(12, 4))
=======
plt.grid()
plt.show()

plt.figure(figsize=(12, 8))
>>>>>>> origin/dev-incorporate-transformer
reward_forward_subdata = reward_forward_data
plt.subplot(211)
plt.plot(reward_forward_subdata, marker='.', linestyle='-')
plt.ylabel('reward forward subdata')
plt.grid()
reward_ctrl_subdata = reward_ctrl_data
plt.subplot(212)
plt.plot(reward_ctrl_subdata, marker='.', linestyle='-')
plt.ylabel('reward ctrl subdata')
plt.grid()
<<<<<<< HEAD
plt.tight_layout()
plt.savefig('saved_plots/reward_data_subplots.png')
plt.close()
=======
plt.show()
>>>>>>> origin/dev-incorporate-transformer
print('sum of reward forward: ', np.sum(reward_forward_subdata))
print('sum of reward ctrl: ', np.sum(reward_ctrl_subdata))

plt.figure(figsize=(12, 5))
plt.subplot(311)
plt.plot(predicted_friction_data, marker='.', linestyle='-')
plt.plot(friction_data, marker='.', linestyle='-')
print(np.mean(predicted_friction_data),np.mean(friction_data))
print("----------------------")
print("friction loss:",np.mean((predicted_friction_data - friction_data))) 
plt.ylabel('friction')
plt.grid()
plt.subplot(312)
plt.plot(predicted_damping_c_data, marker='.', linestyle='-')
plt.plot(damping_c_data, marker='.', linestyle='-')
print("damping loss:",np.mean((predicted_damping_c_data - damping_c_data))) 
plt.ylabel('damping_c')
plt.grid()
plt.subplot(313)
plt.plot(predicted_stiffness_c_data, marker='.', linestyle='-')
plt.plot(stiffness_c_data, marker='.', linestyle='-')
print(stiffness_c_data[0])
print("stiffness loss:",np.mean((predicted_stiffness_c_data - stiffness_c_data))) 
plt.ylabel('stiffness_c')
plt.grid()
plt.tight_layout()
plt.savefig('saved_plots/physical_parameters_comparison.png')
plt.close()