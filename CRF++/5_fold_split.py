import codecs
import sys
import numpy as np
from sklearn.model_selection import KFold
#把数据集5-Fold 交叉验证

#间隔号： "·"
def kFold(n=6000, n_folds=10, shuffle=False):
    folds = []
    base = list(range(n))
    for i in range(n_folds):
        test = base[i*n/n_folds:(i+1)*n/n_folds]
        train = list(set(base)-set(test))
        folds.append([train,test])
    return folds


def main():

    input_file = sys.argv[1]
    train_file = sys.argv[2]
    test_file = sys.argv[3]
    input_data = codecs.open(input_file,'r','utf-8')
    train_data = codecs.open(train_file,'w','utf-8')
    test_data = codecs.open(test_file,'w','utf-8')
    lines = np.array(input_data.readlines())
    #assert len(lines) == 22837
    kf = KFold(5,shuffle=True)
    x = list(range(len(lines)))
    a=kf.split(x)
    
    for train_index, test_index in a:
        trainlines , testlines = lines[train_index] , lines[test_index]

        for line in trainlines:
            train_data.writelines(line)
        for line in testlines:
            test_data.writelines(line)
        break





if __name__ == '__main__':
    main()