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
	(two (cadr pair))
	(one-diff (- (cadr one) (car one)))
	(two-diff (- (cadr two) (car two))))
    (if (> one-diff two-diff)
	(and (<= (car one) (car two)) (>= (cadr one) (cadr two)))
      (and (<= (car two) (car one)) (>= (cadr two) (cadr one))))))

(let ((input (parse-input (f-read "input"))))
  (apply #'+ (mapcar (lambda (x) (if x 1 0)) (mapcar #'num-to-score input))))
