#install.packages("tidyverse")
library(tidyverse)
resimpares <- NULL
for (vertices in list(33,35,37,39,41,43,45,47))  {  # ,37,39,41,43,45,47
  matriz <- NULL
  v <- vertices -1 
  for (i in 0:v) {
    if(i%%2==0)  # Si al dividir por 2 sale 0
      file <- c("trans",vertices,".",i,".g6.ao")
      tabla <- read_tsv(paste(file,collapse = ""),col_names=FALSE)
      tabla$X4 <- (2 * tabla$X2) / (tabla$X2 + (vertices/tabla$X3))
      mini <- min(tabla$X4)
      tabla.df <- as.data.frame(tabla)
      fichero <- c("trans",vertices,".",i,".g6.ao.tsv")
      write_tsv(tabla.df,paste(fichero,collapse = ""),col_names=FALSE)
      fila <- c(vertices,i,mini)
      matriz <- rbind(matriz,fila) }
  minivertices <- min(matriz[,3])
  resimpares <- rbind(resimpares,c(vertices,minivertices))
}
resimpares.df <- as.data.frame(resimpares)
write_tsv(resimpares.df, "res.impares.tsv" )

