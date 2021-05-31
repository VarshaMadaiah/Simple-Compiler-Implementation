# Simple Compiler
Its a simple compiler which compiles a toy language into machine codes
## Requirements
* [Anaconda](https://www.anaconda.com/products/individual#Downloads)
* LLVMlite 
```conda install --channel=numba llvmlite```
* RPLY 
```conda install -c conda-forge rply```
* LLC ``` sudo apt install llvm ```
* GCC ``` sudo apt install gcc ```

## Programing Language Preview
```
print(4 + 4*3 - 2*2);
```
>! This is only  a basic implementation of language .More changes are awaited.

## Steps to recreate in your computer

* **Step 1** : Make sure you have all Requirements
* **Step 2** : Run ``` python main.py ```
* **Step 3** : Run ``` llc -relocation-model=pic -filetype=obj output.ll```
* **Step 4** : Run ``` gcc output.o -o output```
Now the object code is generated as output
* **Step 5** : Run the generated executable using ```./output```
