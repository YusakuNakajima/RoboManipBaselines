from multimodal_robot_model.diffusion_policy import RolloutDiffusionPolicy
from multimodal_robot_model.common.rollout import RolloutRealUR5eGear

class RolloutDiffusionPolicyRealUR5eGear(RolloutDiffusionPolicy, RolloutRealUR5eGear):
    pass

if __name__ == "__main__":
    robot_ip = "192.168.11.4"
    rollout = RolloutDiffusionPolicyRealUR5eGear(robot_ip)
    rollout.run()
