import pybullet as pb
from time import sleep
import pybullet_data

# feel free to import any thing else you might need

SIM_FREQUENCY = 60.0
GRAVITATIONAL_ACC = -9.81

def setup_sim():
    client = pb.connect(pb.GUI)
    pb.setAdditionalSearchPath(pybullet_data.getDataPath())

    pb.setGravity(0, 0, GRAVITATIONAL_ACC)
    planeId = pb.loadURDF("plane.urdf")
    return client

def load_model(model_path, model_position, model_orientation, friction):
    # Implement the model loading method here
    pass

def main():
    # setup pybullet
    client = setup_sim()

    # load models

    try:
        while True:
            #do some sim logic, move models, etc
            
            pb.stepSimulation()
            sleep(1.0/SIM_FREQUENCY)

    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        pb.disconnect()

if __name__ == "__main__":
    main()