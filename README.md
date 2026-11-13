
# HallVoltage

A Python implementation of the **Hall Effect**, featuring calculations for **Hall Voltage** and **Hall Angle**.

## Project Structure

```text
HallVoltage/
├── HallVoltAng.py
├── HallVoltAngimproved.py
├── README.md
├── LICENSE
└── .gitignore
```

## Overview

The **Hall Effect** is the development of a potential difference across a conductor or semiconductor when an electric current flows through it in the presence of a perpendicular magnetic field.

This project provides two implementations:

- **HallVoltAng.py** – Original implementation for calculating Hall Voltage.
- **HallVoltAngimproved.py** – Extended implementation with an interactive menu for calculating both Hall Voltage and Hall Angle.

## Physics and Mathematical Formulas

### 1. Hall Voltage

The Hall Voltage is calculated using:

$$
V_H = \frac{IB}{net}
$$

Where:

| Symbol | Description | SI Unit |
|:---:|---|---|
| $V_H$ | Hall Voltage | Volt (V) |
| $I$ | Electric Current | Ampere (A) |
| $B$ | Magnetic Field | Tesla (T) |
| $n$ | Charge Carrier Density | m$^{-3}$ |
| $e$ | Elementary Charge | Coulomb (C) |
| $t$ | Conductor Thickness | Metre (m) |

The elementary charge is:

$$
e = 1.6 \times 10^{-19}\ C
$$

### 2. Hall Angle

The Hall Angle is calculated using:

$$
\theta_H = \tan^{-1}(\mu B)
$$

Where:

| Symbol | Description | SI Unit |
|:---:|---|---|
| $\theta_H$ | Hall Angle | Radians |
| $\mu$ | Charge Carrier Mobility | m$^2$/(V·s) |
| $B$ | Magnetic Field | Tesla (T) |

The improved implementation uses Python's `math.atan()` function to calculate the inverse tangent.

## Requirements

- **Python 3.x**
- No external dependencies.
- Uses Python's built-in `math` module.

## Installation

Clone the repository:

```bash
git clone https://github.com/AntiEntity314/HallVoltage.git
```

Navigate to the project directory:

```bash
cd HallVoltage
```

## Usage

### Original Implementation

Run:

```bash
python HallVoltAng.py
```

This executes the original Hall Voltage calculator.

### Improved Implementation

Run:

```bash
python HallVoltAngimproved.py
```

The improved implementation provides an interactive menu:

```text
Enter 0 to find Hall Voltage or Enter 1 to find Hall Angle:
```

- Enter `0` to calculate Hall Voltage.
- Enter `1` to calculate Hall Angle.

The program subsequently prompts for the physical quantities required for the selected calculation.

## Input Format

Physical quantities are entered using **scientific notation**, with the numerical value and its power of 10 supplied separately.

For example, to represent:

$$
I = 2 \times 10^{-3}\ A
$$

Enter:

```text
Current: 2
Power of 10: -3
```

This input convention makes it convenient to work with the very small and large quantities commonly encountered in physics.

## Example Calculation

Consider the following parameters:

| Parameter | Value |
|---|---:|
| Current | $2 \times 10^{-3}$ A |
| Magnetic Field | $0.5$ T |
| Charge Carrier Density | $1 \times 10^{22}$ m$^{-3}$ |
| Elementary Charge | $1.6 \times 10^{-19}$ C |
| Conductor Thickness | $1 \times 10^{-3}$ m |

Using:

$$
V_H = \frac{IB}{net}
$$

Substituting the values:

$$
V_H =
\frac{(2 \times 10^{-3})(0.5)}
{(1 \times 10^{22})(1.6 \times 10^{-19})(1 \times 10^{-3})}
$$

Therefore:

$$
\boxed{V_H = 6.25 \times 10^{-4}\ V}
$$

## Limitations

- Inputs are expected to be numerical values.
- Physical quantities must be provided in consistent SI units.
- The Hall Angle implementation requires correct scientific notation scaling.
- The programs currently use a command-line interface.
- The calculations assume standard Hall Effect geometry.

## Future Improvements

- Improved input validation and error handling.
- Automatic scientific notation parsing.
- Hall Angle output in both radians and degrees.
- Graphical user interface.
- Additional calculations related to semiconductor physics.

## License

This project is distributed under the **MIT License**. See the `LICENSE` file for details.

## Author

**AntiEntity314**

GitHub: [AntiEntity314](https://github.com/AntiEntity314)

Repository: [HallVoltage](https://github.com/AntiEntity314/HallVoltage)
