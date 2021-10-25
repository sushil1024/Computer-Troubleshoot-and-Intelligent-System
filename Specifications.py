#importing platform to access platform's data such as hardware, operating system, etc.
import platform

#assigning platform to my_system
my_system = platform.uname()

#operating system
print(f"System: {my_system.system}")

#computer user name
print(f"Node Name: {my_system.node}")

#release of os
print(f"Release: {my_system.release}")

#version of os
print(f"Version: {my_system.version}")

#processor type
print(f"Machine: {my_system.machine}")

#processor family information
print(f"Processor: {my_system.processor}")