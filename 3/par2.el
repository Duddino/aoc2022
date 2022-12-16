(defun str-to-nums (str)
   (mapcar
    (lambda (x)
      (if (<= x ?Z) 
	  (+ (- x ?A) 27)
	(1+ (- x ?a))))
    (string-to-vector str)))

(defun group-by-three (list)
  (reduce
   (lambda (acc x)
     (if (length= (car acc) 3)
	 (cons (list x) acc)
       (cons (cons x (car acc)) (cdr acc))))
   list :initial-value nil))

(defun parse-input (str)
  (group-by-three (mapcar #'str-to-nums (split-string str "\n"))))


(defun find-common-item (vec1 vec2 vec3)
  (reduce
   (lambda (acc v)
     (if acc
	 acc
       (let
	   ((first (cl-find v vec2))
	    (second (cl-find v vec3)))
	 (when (and first second) v))))
   vec1
   :initial-value nil))

(let
    ((input (parse-input (f-read "input"))))
  (apply #'+ (mapcar
   (lambda (x)
     (find-common-item (car x) (cadr x) (caddr x)))
   input)))
