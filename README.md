# Abaqus_multiple_job_execution
A macro created for Abaqus user to execute consecutive simulations.

-------------English-----------------
Instructions

1- Change the contents of variable "nome_arquivo" by inserting a string vector containing the names of the CAE files that have the simulations. The extension must be omitted.
ex:
file_name = ["file_name1", "file_name2", "file_name3"]

2- Change the contents of the "nomes_job" variable by inserting a string vector containing the names of the jobs to be executed
ex:
filename = ["filename2", "filename2", "filename3"]

3- Change the contents of the variable "caminho" by inserting a string with the path of the simulation files. Note that every file must be in the same directory.

Other notes:
1- All models must be named "Model-1" in the simulation archives
2- All jobs must have different names
3- CORRECTLY name files, job and path. Do not put \ at the end of the path.

------------Portugues-----------------
Instruções

1- Alterar o conteúdo da variável "nome_arquivo" inserindo um vetor de strings contendo os nomes dos arquivos CAE que possuem as simulações. A extensão deve ser omitida.
ex:
nome_arquivo=["nome_arquivo1","nome_arquivo2","nome_arquivo3"]

2- Alterar o conteúdo da variável "nomes_job" inserindo um vetor de strings contendo os nomes dos jobs a serem executados
ex: 
nome_arquivo=["nome_job1","nome_job2","nome_job3"]

3- Alterar o conteúdo da variável "caminho" inserindo uma string com o caminho dos arquivos de simulação. Note que todos precisam estar no mesmo diretório.

Observações
1- todos os modelos devem ser nomeados "Model-1" nos arquovos de simulação
2- todos os jobs precisam estar com nomes diferentes
3- nomear arquivos e job e caminho CORRETAMENTE nao colocar \ no final do caminho
