import random
import math

DIM=10
NSAMPLES=1000

def createNeuron():
        weights=[]
        threshold=random.randint(0,DIM)
        for i in range(0,DIM):
                weights=weights+[random.randint(0,1)]
        return weights, threshold

def feedforward(sample, weights, threshold):
        sum=0
        for i in range(0,DIM):
                sum=sum+(sample[i]*weights[i])
        return (sum>=threshold)

def experiment():
        # create data 
        data=[]
        samples=[]
        for i in range(0,NSAMPLES):
                samples=[]
                for j in range(0,DIM+1):
                        samples=samples+[random.randint(0,1)]
                data=data+[samples]
        print("Generated",NSAMPLES,"samples with",DIM,"dimensions.")

        # create hidden layers
        correct=[0] * NSAMPLES        
        tps=0
        neuroncount=0
        while (tps<NSAMPLES):
                neuroncount=neuroncount+1
                neuron=createNeuron()
                redundant=1
                for i in range(0, NSAMPLES):
                        if (correct[i]):
                                continue
                        sample=data[i]
                        if (feedforward(sample,neuron[0],neuron[1])==sample[DIM]):
                                correct[i]=1
                                tps=tps+1
                                redundant=0
                if (redundant):
                        neuroncount=neuroncount-1
                        continue
                print(neuroncount,"neuron accuracy:",(tps/NSAMPLES)*100,"%")
        print("Expected number of hidden neurons:",math.ceil(math.log(NSAMPLES,2))," actual:", neuroncount)
        return neuroncount

if __name__ == "__main__":
        numruns=1000
        numneurons=0
        for i in range(0,numruns):
                numneurons=numneurons+experiment()
        print("Over",numruns,"runs:")
        print("Expected number of hidden neurons:",math.ceil(math.log(NSAMPLES,2))," actual avg:", numneurons/numruns)



