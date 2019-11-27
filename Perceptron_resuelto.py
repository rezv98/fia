#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import array, array_equal, dot, where


# In[6]:


def train(set_input,set_output,set_weight):
	salida = array([[0.0,0.0,0.0,0.0]]).T
	count_epoca = 1
	
	while (not(array_equal(salida,set_output))):
		output_epoca = []
		nro_fila = 0
		print(' -----EPOCA: ',count_epoca,'------')
		for fila_epoca in set_input:
			print('Entrada',fila_epoca)
			real = predict(fila_epoca,set_weight)
			print('real: ',real)
			deseada = set_output[nro_fila,:]
			print('deseada: ',deseada)
			error = deseada - real		
			print('error: ',error)
			if(error[0] != [0]):
				set_weight = modify_weight(set_weight,fila_epoca,error)
			output_epoca.append(real[0])
			nro_fila = nro_fila+1
			print('Peso:\n',set_weight,'\n')
			print('------------------------------')
		salida = array([output_epoca]).T	
		count_epoca = count_epoca + 1
		print('Salida:\n',salida,'\n')
		print('---------FIN --------------')

	
def predict(fila,weight):
	return where(dot(fila,weight)>=0,1,-1)

def modify_weight(weight,fila,e):
	return weight+(e*(array([fila]).T))

def main():

	BIAS = 1
	training_set_data_input = array([[-1,-1,BIAS],[1,-1,BIAS],[-1,1,BIAS],[1,1,BIAS]])
	training_set_data_output = array([[-1,-1,-1,1]]).T
	set_data_weight = array([[1,1,0.5]]).T
	print('Training_data_input:\n',training_set_data_input,'\n')
	print('Training_data_output:\n',training_set_data_output,'\n')	
	print('Init_weight:\n',set_data_weight,'\n')

	train(training_set_data_input,training_set_data_output,set_data_weight)

main()


# In[ ]:




