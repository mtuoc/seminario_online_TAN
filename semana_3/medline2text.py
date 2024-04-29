import sys
import os
from bs4 import BeautifulSoup
import codecs
import glob

import os
import sys

rootdir = sys.argv[1]

for path, currentDirectory, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".html") or file.endswith(".htm"):
            fullpath=os.path.join(path, file)
            try:
                entrada=codecs.open(fullpath,"r",encoding="utf-8")
                html=" ".join(entrada.readlines())
                htmlParse = BeautifulSoup(html, 'html.parser')
                try:
                    lang=htmlParse.html["lang"]
                    outdir="text-"+lang
                    if not os.path.exists(outdir):
                        os.makedirs(outdir)
                    #we search for <link rel="alternate" hreflang="en" href="https://www.msdmanuals.com/home/hormonal-and-metabolic-disorders/acid-base-balance/acidosis"> to find the English file name
                    result = htmlParse.find("link", {"rel" : "alternate","hreflang":"en"})
                    try:
                        href=result["href"]
                        outname=href.split("/")[-1].replace(".html","")+"-"+lang+".txt"
                        outpath=os.path.join(outdir,outname)
                        print(outpath)
                        sortida=codecs.open(outpath,"w",encoding="utf-8")
                        titles1 = htmlParse.find_all('h1')
                        titles2 = htmlParse.find_all('h2')
                        titles3 = htmlParse.find_all('h2')
                        paras = htmlParse.find_all('p')
                        
                        for line in titles1:
                            line=line.get_text()
                            line=line.lstrip().rstrip()
                            if len(line)>0:
                                sortida.write(line+"\n")
                        for line in titles2:
                            line=line.get_text()
                            line=line.lstrip().rstrip()
                            if len(line)>0:
                                sortida.write(line+"\n")
                        
                        for line in titles3:
                            line=line.get_text()
                            line=line.lstrip().rstrip()
                            if len(line)>0:
                                sortida.write(line+"\n")
                        
                        for line in paras:
                            line=line.get_text()
                            line=line.lstrip().rstrip()
                            if len(line)>0:
                                sortida.write(line+"\n")
                        
                    except:
                        pass
                except:
                    pass
            except:
                pass
