import numpy as np
import matplotlib.pyplot as plt

# motor properties
J = 1e-3  # inertia (kg * m^2)
R = 0.141  # resistance (Ohms)
k = 0.005882  # motor constant (N * m / A)
mu = 2.293e-6  # friction coefficient (N * m / rad / s)


def motor_model(time_step, voltage, speed, load):
    # Simple motor model of a dc motor
    # Inputs:
    #   time_step of simulation (s)
    #   voltage applied to the motor (V)
    #   motor speed at current time (rad/s)
    #   torque load on motor (Nm)
    # Output:
    #   updated motor speed (rad/s)
    alpha = (1.0 / J) * ((k / R) * (voltage - k * speed) - mu * speed - load)
    return speed + alpha * time_step


def main():
    # simulation parameters
    begin_time = 0.0
    end_time = 15.0
    time_step = 0.01

    # initial conditions
    init_speed = 0.0
    init_voltage = 12.0

    # reference speed
    # try varying reference speeds and loads
    reference_speed = 800.0  # rad/s
    motor_load = 0.0  # Nm

    # storage of solutions
    total_iters = int((end_time - begin_time) / time_step)
    times = np.array(np.linspace(begin_time, end_time, total_iters))
    voltages = []
    speeds = []

    speed = init_speed
    applied_voltage = init_voltage
    for time in times:
        # run your pid controller here here

        # step the simulation
        speed = motor_model(time_step, applied_voltage, speed, motor_load)

        # save states
        voltages.append(applied_voltage)
        speeds.append(speed)


if __name__ == "__main__":
    main()