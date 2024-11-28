import numpy as np
import gymnasium as gym
import pinocchio as pin
import multimodal_robot_model
from multimodal_robot_model.teleop import TeleopBase
from multimodal_robot_model.common import MotionStatus

class TeleopIsaacUR5eChain(TeleopBase):
    def setup_env(self):
        self.env = gym.make(
            "multimodal_robot_model/IsaacUR5eChainEnv-v0",
            render_mode="human"
        )
        self.demo_name = self.args.demo_name or "IsaacUR5eChain"

    def set_arm_command(self):
        if self.data_manager.status in (MotionStatus.PRE_REACH, MotionStatus.REACH):
            target_pos = self.env.unwrapped.get_link_pose("chain_end", "box")[0:3]
            if self.data_manager.status == MotionStatus.PRE_REACH:
                target_pos[2] += 0.22 # [m]
            elif self.data_manager.status == MotionStatus.REACH:
                target_pos[2] += 0.14 # [m]
            self.motion_manager.target_se3 = pin.SE3(np.diag([-1.0, 1.0, -1.0]), target_pos)
        else:
            super().set_arm_command()

    def set_gripper_command(self):
        if self.data_manager.status == MotionStatus.GRASP:
            self.motion_manager.gripper_pos = 150.0
        else:
            super().set_gripper_command()

if __name__ == "__main__":
    teleop = TeleopIsaacUR5eChain()
    teleop.run()
