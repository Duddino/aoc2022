(defun parse-input (str)
  (mapcar
   (lambda (x) (mapcar #'string-to-number (split-string x "\n")))
   (split-string str "\n\n")))


(let* ((input (parse-input (f-read "input")))
  (sum-calorie (mapcar
   (lambda (x) ; x = list of string
     (apply '+ x))
   input)))
  (car (sort sum-calorie #'>)))
