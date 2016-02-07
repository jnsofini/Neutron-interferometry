## This function creates a special matrix object that can cache its inverse.
## If the inverse has been computed it simply cache it

## Create a matrix element that can have multiple attributes. It stores its inverse
## once it is computed and these can be access with the attributes and methods.

makeCacheMatrix <- function(x = matrix()) {
  
  minv <- NULL
  set <- function(y) {
    x <<- y
    minv  <<- NULL
  }
  get <- function() x
  setinverse <- function(inverem) minv  <<- inverem
  getinverse <- function() minv 
  list(set = set, get = get,
       setinverse = setinverse,
       getinverse = getinverse)

}


##Takes a matrix which is an object of makeCacheMatrix and compute it inverse if not found
##in it inverse attribute and the set the invese attribute to computed value.

cacheSolve <- function(x, ...) {
        ## Return a matrix that is the inverse of 'x'
  minv  <- x$getinverse()
  if(!is.null(minv )) {
    message("getting cached data")
    return(minv )
  }
  data <- x$get()
  minv  <- solve(data, ...)
  x$setinverse(minv )
  minv 
}

