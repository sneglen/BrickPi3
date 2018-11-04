#! /bin/bash

PIHOME=/home/pi
DEXTER=Dexter
DEXTER_PATH=$PIHOME/$DEXTER
BRICKPI3_DIR=$DEXTER_PATH/BrickPi3

# the following option specifies which BrickPi3 github branch to use
selectedbranch="master"

check_if_run_with_pi() {
  ## if not running with the pi user then exit
  if [ $(id -ur) -ne $(id -ur pi) ]; then
    echo "BrickPi3 installer script must be run with \"pi\" user. Exiting."
    exit 7
  fi
}

clone_brickpi3() {
  echo "Cloning BrickPi3 repository"

  # create folders recursively if they don't exist already
  # we use sudo for creating the dir(s) because on older versions of R4R
  # the sudo command is used, and hence we need to be sure we have write permissions.
  sudo mkdir -p $DEXTER_PATH
  # still only available for the pi user
  # shortly after this, we'll make it work for any user
  sudo chown pi:pi -R $DEXTER_PATH
  cd $DEXTER_PATH

  # it's simpler and more reliable (for now) to just delete the repo and clone a new one
  # otherwise, we'd have to deal with all the intricacies of git

  sudo rm -rf $BRICKPI3_DIR
  # MT for testing temporarily use mattallen37 repo for cloning.
  #git clone --quiet --depth=1 -b $selectedbranch https://github.com/DexterInd/BrickPi3.git
  git clone --quiet --depth=1 -b $selectedbranch https://github.com/sneglen/BrickPi3.git
  cd $BRICKPI3_DIR
  echo "Done cloning BrickPi3 repository"
}

################################################
########               MAIN             ########
################################################
check_if_run_with_pi
clone_brickpi3

exit 0
