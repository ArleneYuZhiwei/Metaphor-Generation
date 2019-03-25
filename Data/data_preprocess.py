# -*- coding: utf-8 -*-
import nltk
import string
import os
exclude = set(string.punctuation)
word_forward=[]
forward_re=[]
back=[]

with open ('sentence.txt','r+') as f:
    for line in f:
        sen=[i.lower() for i in line.decode('utf-8').strip().split(' ') if i not in exclude]
        words=[]
        for a in sen:
            if any(char.isdigit() for char in a):
                words.append('#')
            else:
                words.append(a)
        line = ' '.join(i for i in words)
        text = nltk.word_tokenize(line)
        text_tags = nltk.pos_tag(text) 
        n_n={}
        adj_n={}
        n_v={}
        index={}
        for i in range(3,len(text_tags)):
            if len(n_n)<2 and (text_tags[i][1]=='NN' or text_tags[i][1]=='NNS') :
                if (i== len(text_tags)-1) or (i!= len(text_tags)-1 and text_tags[i+1][1]!='NN' and text_tags[i+1][1]!='NNS'):
                    if 'one' not in n_n:
                        n_n['one']=text_tags[i][0]
                        index["n_n_one"]=i
                    elif 'two' not in n_n:
                        n_n['two']=text_tags[i][0]
                        index["n_n_two"]=i             
            if len(adj_n)<2 and (text_tags[i-1][1]=='JJ' or text_tags[i-1][1]=='JJR' or text_tags[i-1][1]=='JJS'or text_tags[i-1][1]=='VBG' or text_tags[i-1][1]=='VBN'  )and (text_tags[i][1]=='NN' or text_tags[i][1]=='NNS'):  
                    adj_n['one']=text_tags[i-1][0]
                    index["adj_n_one"]=i-1
                    adj_n['two']=text_tags[i][0]
                    index["adj_n_two"]=i
            if len(n_v)<2 and (text_tags[i-1][1]=='NN' or text_tags[i-1][1]=='NNS') and \
            (text_tags[i][1]=='VBZ ' or text_tags[i][1]=='VBP'  or text_tags[i][1]=='VB'):           
                    n_v['one']=text_tags[i-1][0]
                    index["n_v_one"]=i-1
                    n_v['two']=text_tags[i][0]
                    index["n_v_two"]=i
            if len(n_v)<2 and (text_tags[i-2][1]=='NN' or text_tags[i-2][1]=='NNS') and ((text_tags[i-1][1]=='MD' or text_tags[i-1][1]=='VBD') and (text_tags[i][1]=='VB' or text_tags[i][1]=='VBG' or text_tags[i][1]=='VBN')): 
                    n_v['one']=text_tags[i-2][0]
                    index["n_v_one"]=i-2
                    n_v['two']=text_tags[i][0]
                    index["n_v_two"]=i
        if len(n_n) == 2:
            forward=text_tags[:index["n_n_one"]+1]
            backward=text_tags[index["n_n_one"]+1:]
            word_forward.append(''.join(i for i in n_n['two'])+' '+' '.join(i[0] for i in forward)+'\n')
            back.append(' '.join(j[0] for j in backward)+'\n')
            re=list(reversed(forward))
            forward_re.append(' '.join(i[0] for i in re)+'\n')
            print (line)
        elif len(adj_n) == 2:
            forward=text_tags[:index["adj_n_one"]+1]
            backward=text_tags[index["adj_n_one"]+1:]
            word_forward.append(''.join(i for i in adj_n['two'])+' '+' '.join(i[0] for i in forward)+'\n')
            back.append(' '.join(j[0] for j in backward)+'\n')
            re=list(reversed(forward))
            forward_re.append(' '.join(i[0] for i in re)+'\n')
            print (line)
        elif len(n_v) == 2:
            forward=text_tags[:index["n_v_one"]+1]
            backward=text_tags[index["n_v_one"]+1:]
            word_forward.append(''.join(i for i in n_v['two'])+' '+' '.join(i[0] for i in forward)+'\n')
            back.append(' '.join(j[0] for j in backward)+'\n')
            re=list(reversed(forward))
            forward_re.append(' '.join(i[0] for i in re)+'\n')
            print (line)

        else:
            pass

word_forward_f = open('word_forward_f','w+')   
word_forward_f.write(''.join(i.encode('utf-8') for i in word_forward))
word_forward_f.close()
forward_re_f = open('forward_re_f','w+')
forward_re_f.write(''.join(j.encode('utf-8') for j in forward_re))
forward_re_f.close()
backward_f=open('backward_f','w+')
backward_f.write(''.join(k.encode('utf-8') for k in back))
backward_f.close()


            
            
            
            