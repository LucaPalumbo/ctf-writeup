function() {
  library('png')
  library('colorspace')

  image_path <- "./flag.png"
  n <- 50

  x <- readPNG(image_path)

  y <- rgb(x[,,1], x[,,2], x[,,3])
  yg <- desaturate(y)
  yn <- col2rgb(yg)[1, ]/255
  dim(y) <- dim(yg) <- dim(yn) <- dim(x)[1:2]

  V <- prcomp(yn)

  X <- t(rbind(t(V$rotation[,1:n]), t(V$x[,1:n])))
  X <- X - 42
  X <- X / 5
  X <- X + 69
  X <- X * 3

  load("something")

  if (max(abs(X - mtov)) < 6e-5) {
    cat("Yes!")
  } else {
    cat("Try harder")
    cat(max(abs(X - mtov)))
  }
}