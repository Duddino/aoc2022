(defun parse-input (x)
  (mapcar
   (lambda (x)
     (mapcar
      (lambda (x)
	(mapcar
	 (lambda (x) (string-to-number x))
	 (split-string x "-")))
      (split-string
       x
       ",")))
   (split-string x "\n")))

(defun num-to-score (pair)
  (let* ((one (car pair))
	(two (cadr pair)))
    (not (if (< (car one) (car two))
	(and (< (cadr one) (car two)))
      (and (< (cadr two) (car one)))))))

(let ((input (parse-input (f-read "input"))))
  (apply #'+ (mapcar (lambda (x) (if x 1 0)) (mapcar #'num-to-score input))))

