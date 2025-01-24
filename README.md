#Linear Algebra for AI - COVID-19 Spread Model  

## 🧠 Theory  
- **Vectors**: Ordered lists of numbers (e.g., `[1, 0, 0]` = initial infections).  
- **Matrices**: Grids representing relationships (e.g., travel between regions).  
- **Matrix Exponentiation**: Models multi-step processes (e.g., infections over days).  

## 💻 Code  
Simulated COVID-19 spread across 3 regions using adjacency matrices and matrix exponentiation.  

### How It Works  
1. **Adjacency Matrix**:  
   ```python  
   A = [
     [0.0, 0.3, 0.1],  # Region A  
     [0.2, 0.0, 0.4],  # Region B  
     [0.1, 0.2, 0.0]   # Region C  
   ]  
