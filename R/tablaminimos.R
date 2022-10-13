# install.packages("tidyverse")
library(tidyverse)
res <- NULL
for (vertices in list(32,34,36,38,40,42,44,46))  {
  matriz <- NULL
  v <- vertices -1 
  for (i in 0:v) {
    file <- c("trans",vertices,".",i,".g6.ao")
    tabla <- read_tsv(paste(file,collapse = ""),col_names=FALSE)
    tabla$X4 <- (2 * tabla$X2) / (tabla$X2 + (vertices/tabla$X3))
    tabla.df <- as.data.frame(tabla)
    fichero <- c("trans",vertices,".",i,".g6.ao.tsv")
    write_tsv(tabla.df,paste(fichero,collapse = ""),col_names=FALSE)
    mini <- min(tabla$X4)
    fila <- c(vertices,i,mini)
    matriz <- rbind(matriz,fila) }
  minivertices <- min(matriz[,3])
  res <- rbind(res,c(vertices,minivertices)) 
}
respares.df <- as.data.frame(res)
write_tsv(respares.df,"res.pares.csv")
