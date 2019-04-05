import os

URLS_DEFACED = './defaced.txt'
URLS_LEGITIMATE = './legitimate.txt'

PATH_DEFACED = './defaced/'
PATH_LEGITIMATE = './legitimate/'

PATH_RPTIVE_DFCED = './representativeDefaced/'
PATH_RPTIVE_LGTIMATE = './representativeLegitimate/'

input = 'python script.py ' + URLS_DEFACED + ' ' + PATH_DEFACED
os.system(input)

input = 'python scriptRepresentativeImage.py ' + PATH_DEFACED + ' ' + PATH_RPTIVE_DFCED
os.system(input)

input = 'python script.py ' + URLS_LEGITIMATE + ' ' + PATH_LEGITIMATE
os.system(input)

input = 'python scriptRepresentativeImage.py ' + PATH_LEGITIMATE + ' ' + PATH_RPTIVE_LGTIMATE
os.system(input)