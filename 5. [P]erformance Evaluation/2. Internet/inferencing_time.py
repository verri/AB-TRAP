import timeit
import random
from pickle import load
from pandas import DataFrame

models = ['knn', 'rf', 'dt', 'lr', 'xgb', 'mlp', 'nb', 'svm']

features = ['ip.id', 'ip.flags.df', 'ip.ttl', 'ip.len', 'ip.dsfield', 'tcp.srcport', 'tcp.seq', 'tcp.len', 'tcp.hdr_len',
           'tcp.flags.fin', 'tcp.flags.syn', 'tcp.flags.reset', 'tcp.flags.push', 'tcp.flags.ack', 'tcp.flags.urg',
           'tcp.flags.cwr', 'tcp.window_size', 'tcp.urgent_pointer', 'tcp.options.mss_val']

preprocess = load(open("../../4. [R]ealiz[A]tion/2. Internet/Models/preprocessor.pkl", "rb"))

# generating random attributes 
pkt = [random.random() for i in range(0,len(features))]

for model in models:
    pickle_model = load(open("../../4. [R]ealiz[A]tion/2. Internet/Models/"+model+".pkl","rb"))

    df = DataFrame([pkt], columns=features)

    if model == "xgb":
        cols = pickle_model.get_booster().feature_names
        df = df[cols]

    X = preprocess.transform(df)
    X = DataFrame(X, columns=features)

    print("The average inference time taken by {} is {:.2f} ms".format(model, timeit.timeit('pickle_model.predict(X)',
                                                                               setup="from __main__ import pickle_model, X",
                                                                               number=1000)))
