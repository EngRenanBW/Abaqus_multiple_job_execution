nome_arquivo=["exercicio_7_capitulo_4","exercicio_8_capitulo_4","exercicio_21_capitulo_4"] #nao colocar extencao .cae
nomes_job=["exercicio_7_capitulo_4_ERRO","exercicio_8_capitulo_4","exercicio_21_capitulo_4"]
caminho='C:/Users/Renan/Desktop/Macro_rodar_simulacao_seguida'


from abaqus import *
from abaqusConstants import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior


for contador in range(len(nome_arquivo)):
	try:
		#abre cae
		openMdb(pathName=caminho+'\\'+nome_arquivo[contador]+'.cae')

		#executa job
		mdb.jobs[nomes_job[contador]].submit(consistencyChecking=OFF)

		#espera o job completar
		if(nomes_job[contador] in mdb.jobs.keys()):
			mdb.jobs[nomes_job[contador]].waitForCompletion()
	except:
		print("Um erro ocorreou no arquivo "+nome_arquivo[contador])
			
print("terminou")
