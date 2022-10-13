library(readr)
vertices <- 32
matriz <- NULL
v <- vertices -1 
for (i in 0:v) {
  file <- c("trans32.",i,".g6.ao")
  tabla <- read_tsv(paste(file,collapse = ""),col_names=FALSE)
  tabla$X4 <- (2 * tabla$X2) / (tabla$X2 + (vertices/tabla$X3))
  mini <- min(tabla$X4)
  fila <- c(vertices,i,mini)
  matriz <- rbind(matriz,fila) }
minivertices <- min(matriz[,3]) 

