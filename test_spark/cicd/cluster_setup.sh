MODULE_NAME="test_spark"

# download and install conda
wget https://repo.anaconda.com/miniconda/Miniconda2-latest-Linux-x86_64.sh
chmod u+x Miniconda2-latest-Linux-x86_64.sh
./Miniconda2-latest-Linux-x86_64.sh -b -p $HOME/miniconda

echo 'export PATH=~/miniconda/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
conda init
source ~/.bashrc

# attach source code to python path
echo 'export PYTHONPATH=$PYTHONPATH:~/$MODULE_NAME' >> ~/.bashrc
source ~/.bashrc

# replicate environment
conda env create -f $MODULE_NAME/environment.yml

# create log directory
mkdir log

# use vim in terminal
echo "set -o vi" >> ~/.bashrc
source ~/.bashrc

