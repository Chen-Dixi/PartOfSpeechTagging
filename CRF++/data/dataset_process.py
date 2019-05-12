import codecs
import sys
import os



def train(corpus_file):
    input_data = codecs.open(corpus_file,'r',encoding='utf-8')
    output_data = codecs.open("train.data",'w',encoding='utf-8')

    for line in input_data.readlines():
        word_list = line.strip().split()
        for word in word_list:
            word_pos = word.split('/')
            w ,pos = word_pos[0],word_pos[1]
            #处理[ ] 间隔号·
            if w.find('[') >= 0:
                w = w[w.find('[')+1:]
            if pos.find(']') >= 0:
                pos = pos[:pos.find(']')] #像这种机构名称就分开吧[中国/ns  政府/n]nt
            if pos == 'nr': 
                if w.find('·') >= 0:#特殊外国人名
                    namesArray = w.split('·')
                    for name in namesArray:
                        output_data.write(name+"\t"+pos+"\n")
                    continue
            output_data.write(w+"\t"+pos+"\n")
        output_data.write("\n")

    input_data.close()
    output_data.close()
def test(corpus_file):
    input_data = codecs.open(corpus_file,'r',encoding='utf-8')
    output_data = codecs.open("test.data",'w',encoding='utf-8')

    for line in input_data.readlines():        
        word_list = line.strip().split()
        for word in word_list:
            word_pos = word.split('/')
            w ,pos = word_pos[0],word_pos[1]
            #处理[ ] 间隔号·
            if w.find('[') >= 0:
                w = w[w.find('[')+1:]
            if pos.find(']') >= 0:
                pos = pos[:pos.find(']')] #像这种机构名称就分开吧[中国/ns  政府/n]nt
            if pos == 'nr': 
                if w.find('·') >= 0:#特殊外国人名
                    namesArray = w.split('·')
                    for name in namesArray:
                        output_data.write(name+"\t"+pos+"\n")
                    continue
            output_data.write(w+"\t"+pos+"\n")
        output_data.write("\n")

    input_data.close()
    output_data.close()

def main():
    train_corpus_f = sys.argv[1]
    test_corpus_f = sys.argv[2]

    train(train_corpus_f)    
    test(test_corpus_f)

if __name__ == '__main__':
    main()