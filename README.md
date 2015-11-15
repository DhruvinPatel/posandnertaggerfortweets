# POS and NER Tagger for tweets
###TASK: Named entity recognition (NER) and Part of speech (POS) tagging for tweets

More details about training and testing can be found on this link: http://www.cse.iitd.ernet.in/~parags/teaching/col776/assignments/ass3/ass3-b.pdf <br>
Code has 2 trained models present corresponding to NER and POS tasks. They are MODEL_ner, MODEL_pos

###HOW TO RUN:
```bash
./compile.sh
./runpos.sh pos_inputfile pos_outputfile
./runner.sh ner_inputfile ner_outputfile
```

Note: Before running above commands you should have MALLET_INC defined appropriately (i.e. MALLET build directory) and MALLET installed.


###Files present in the present working directory:
* compile.sh
* runpos.sh (to run pos tagger)
* runner.sh (to run ner tagger)
* Writeup.pdf (describes features used in Model building)
* posinputfile (or called the testfile)
* pos_goldfile (contains gold labels)
* nerinputfile (or called the testfile)
* ner_goldfile (contains gold labels)
* MODEL_pos
* MODEL_ner
* format_checker.py
* Fscore_pos.py
* Fscore_ner.py
* posoutputparse.py (intermediate script)
* neroutputparse.py (intermediate script)
* postest.py (intermediate script which builds features)
* nertest.py (intermediate script which builds features)
* brownclusterdata (list of browncluster-id, words)
* nerdatalist (ner-tagged dataset)
* posdatalist (pos-tagged dataset)


###Evaluation:

To evaluate the model by compute Macro F-measure using Fscore_MODEL.py. Following are the commands to use the script:
python Fscore_MODEL.py MODEL_outputfile MODEL_goldfile

(replace MODEL with either pos / ner)











