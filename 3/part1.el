(defun str-to-nums (str)
  (apply
   #'vector
   (mapcar
    (lambda (x)
      (if (<= x ?Z) 
	  (+ (- x ?A) 27)
	(1+ (- x ?a))))
    (string-to-vector str))))

(defun parse-input (str)
  (mapcar
   (lambda (str)
     (let ((len (length str)))
       (list (substring str 0 (/ len 2))
	     (substring str (/ len 2)))))
   (mapcar #'str-to-nums (split-string str "\n"))))

(defun find-common-item (vec1 vec2)
  (reduce
   (lambda (acc v)
     (if acc
	 acc
       (cl-find v vec2)))
   vec1
   :initial-value nil))

(let
    ((input (parse-input (f-read "input"))))
  (apply #'+ (mapcar
   (lambda (x)
     (find-common-item (car x) (cadr x)))
   input)))
