install.packages("tidyverse")
library(tidyverse)
res <- NULL
for (vertices in 11:31)  {
  matriz <- NULL
  file <- c("vtc",vertices,".ata")
  tabla <- read_tsv(paste(file,collapse = ""),col_names=FALSE)
  tabla$X5 <- (2 * tabla$X2) / (tabla$X2 + (tabla$X4))
  tabla.df <- as.data.frame(tabla)
  fichero <- c("vtv",vertices,".ata.tsv")
  write_tsv(tabla.df,paste(fichero,collapse = ""),col_names=FALSE)
  mini <- min(tabla$X5)
  res <- rbind(res,c(vertices,mini)) 
}
resparesmall.df <- as.data.frame(res)
write_tsv(resparesmall.df,"ressmall.pares.csv")
