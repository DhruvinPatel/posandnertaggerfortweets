python postest.py $1
#MALLET_INC="/home/dhruvin/mallet-2.0.8RC2/class:/home/dhruvin/mallet-2.0.8RC2/lib/mallet-deps.jar"

java -cp $MALLET_INC cc.mallet.fst.SimpleTagger --model-file MODEL_pos posoutputfeaturestest > $2

python posoutputparse.py $2 $1


