# Installation
```
# Clone the repository to your computer
git clone https://github.com/alesvcelka1/kube_flask

# Enter the directory
cd kube_flask

# Create a virtual enviroment .venv
python -m venv .venv

# Activate the virtual enviroment
. .venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Build the container
docker build -t test .

# Run the docker container
docker run -p 5000:5000
```
