import re

#[\s][^z\s]*[z][\w]{3}[z][^\s]*
regex = "[\\s][^z\\s]*[z][\w]{3}[z][^\\s]*"

result = re.findall(regex, ' 123123123z23z 1231231z123zfasdsa')
print(result)