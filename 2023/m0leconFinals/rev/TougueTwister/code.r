a = load("something")
mtov <- mtov / 3
mtov <- mtov - 69
mtov <- mtov * 5
mtov <- mtov + 42
n = 50
#  X <- t(rbind(t(V$rotation[,1:n]), t(V$x[,1:n])))
# reverse this
mtov = t(mtov)
rotation <- t(mtov[1:n,])
x <- t(mtov[(n+1):(2*n),])
Xhat = x[,1:n] %*% t(rotation[,1:n])
# create a vec of 256 values all equal to -0.5
vec = rep(-0.3, 256)
Xhat = scale(Xhat, center = vec, scale = FALSE)
Xhat = Xhat*255

write.csv(Xhat, "ziopera.csv", row.names=FALSE)
