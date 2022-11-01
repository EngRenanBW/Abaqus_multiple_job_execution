# Abaqus_multiple_job_execution
A macro created for Abaqus users to execute consecutive simulations.
Uma macro criada para usuários do Abaqus (Simulia) com a finalidade de executar simulações consecutivas.

-------------English-----------------
Instructions

1- Change the contents of the variable "nome_arquivo" by inserting a string vector containing the names of the CAE files with the simulations. The extension must be omitted.
Ex:
file_name = ["file_name1", "file_name2", "file_name3"]

2- Change the contents of the variable "nomes_job" by inserting a string vector containing the names of the jobs to be executed.
Ex:
filename = ["filename2", "filename2", "filename3"]

3- Change the contents of the variable "caminho" by inserting a string containing the path of the simulation files. Note that every file must be in the same directory.

Other notes:
1- All models must be named "Model-1" in the simulation archives;
2- All jobs must have different names;
3- CORRECTLY name the files, jobs and path. Do not insert \ at the end of the path.

------------Português-----------------
Instruções

1- Alterar o conteúdo da variável "nome_arquivo", inserindo um vetor de strings contendo os nomes dos arquivos CAE que possuem as simulações. A extensão deve ser omitida.
Ex:
nome_arquivo=["nome_arquivo1","nome_arquivo2","nome_arquivo3"]

2- Alterar o conteúdo da variável "nomes_job", inserindo um vetor de strings contendo os nomes dos jobs a serem executados.
Ex:
nome_arquivo=["nome_job1","nome_job2","nome_job3"]

3- Alterar o conteúdo da variável "caminho", inserindo uma string com o caminho dos arquivos de simulação. Note que todos os arquivos precisam estar no mesmo diretório.

Observações:
1- Todos os modelos nos arquivos de simulação devem ser nomeados "Model-1";
2- Todos os jobs precisam estar com nomes diferentes;
3- Nomear arquivos, jobs e caminho CORRETAMENTE. Não coloque \ no final do caminho.
