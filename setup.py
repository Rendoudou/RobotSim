from distutils.core import setup

setup(
    version='0.0.0',
    scripts=['scripts/teleop_twist_keyboard.py'],
    packages=['robot_sim_teleop'],
    package_dir={'': 'scripts'}
)