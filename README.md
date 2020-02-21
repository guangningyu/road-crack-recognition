# Environment
- EC2 instance type: g4dn.xlarge
- AMI: Deep Learning AMI (Ubuntu) Version 24.2 (ami-0c49319553bb6ea78)
- Virtual environment: tensorflow_p36

# Data Preparation

*Note: this project uses the data collected in project [Road Damage Detector](https://github.com/sekilab/RoadDamageDetector/), therefore the steps 1-2 can be skipped.*

1. Resize images ([script](scripts/gen_thumbnail.py))
2. Annotate images with [labelImg](https://github.com/tzutalin/labelImg)
