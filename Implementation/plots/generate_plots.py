import json
import matplotlib.pyplot as plt
import numpy as np
import os

def plot_combined_results(exp1_data, exp2_data):
    """
    Genera y guarda graficas combinando los resultados de dos experimentos.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, 'combined_plots')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    all_data = exp1_data + exp2_data
    
    # Metricas a graficar
    metrics = ['iterations', 'function_evaluations', 'gradient_evaluations', 'execution_time', 'distance_to_optimum']
    
    # Extraer datos para cada metodo
    newton_cg_data = {metric: [d['newton_cg'][metric] for d in all_data] for metric in metrics}
    bfgs_data = {metric: [d['bfgs'][metric] for d in all_data] for metric in metrics}
    
    # Crear etiquetas para el eje x
    config_labels = []
    for i in range(len(exp1_data)):
        config_labels.append(f"Exp1-C{i+1}")
    for i in range(len(exp2_data)):
        config_labels.append(f"Exp2-C{i+1}")

    # Generar una grafica para cada metrica
    for metric in metrics:
        plt.figure(figsize=(15, 7))
        
        x = np.arange(len(config_labels))
        width = 0.35
        
        rects1 = plt.bar(x - width/2, newton_cg_data[metric], width, label='Newton-CG')
        rects2 = plt.bar(x + width/2, bfgs_data[metric], width, label='BFGS')
        
        if metric == 'distance_to_optimum':
            plt.yscale('log', base=10)
            plt.ylabel(f"{metric.replace('_', ' ').title()} (Escala Log Base 10)")
        else:
            plt.ylabel(metric.replace('_', ' ').title())
        
        plt.title(f'Comparacion de {metric.replace("_", " ").title()} (Experimentos 1 y 2)')
        plt.xticks(x, config_labels, rotation=45, ha="right")
        plt.legend()
        
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'combined_{metric}_comparison.png'))
        plt.close()

def main():
    """
    Carga los datos de los experimentos y genera las graficas combinadas.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construir rutas absolutas a los archivos de resultados
    exp1_path = os.path.join(script_dir, '..', 'Results', 'results_exp1.json')
    exp2_path = os.path.join(script_dir, '..', 'Results', 'results_exp2.json')

    # Cargar datos del experimento 1
    with open(exp1_path, 'r') as f:
        exp1_data = json.load(f)
    
    # Cargar datos del experimento 2
    with open(exp2_path, 'r') as f:
        exp2_data = json.load(f)

    # Generar graficas combinadas
    plot_combined_results(exp1_data, exp2_data)

    print("Las graficas combinadas han sido generadas y guardadas en la carpeta 'combined_plots'.")

if __name__ == '__main__':
    main()
