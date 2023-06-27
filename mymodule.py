import matplotlib as plt

def draw_histograms(df):
    num_columns = df.columns
    num_cols_count = len(num_columns)
    num_rows = int(num_cols_count/2) + (num_cols_count % 2 > 0)
    
    fig, axes = plt.subplots(num_rows, 2, figsize=(12, 12))
    fig.tight_layout(pad=3.0)
    
    for i, column in enumerate(num_columns):
        row = i // 2
        col = i % 2
        ax = axes[row, col]
        
        ax.hist(df[column], bins='auto')
        ax.set_title(f'Histogram of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        
    plt.show()
