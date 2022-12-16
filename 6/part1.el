(defun are-all-different(str)
  (reduce
   (lambda (acc x)
     (if acc
	 (when (not (member* x (string-to-list acc))) (concatenate 'string acc (list x)))
       nil))
   str :initial-value ""))

(defvar input (f-read "input"))

(reduce
 (lambda
   (acc x)
   (if (caar acc)
       acc
     (let
	 ((new-string (concatenate 'string (substring (cdr acc) 1) (list x))))
       (cons (cons (are-all-different new-string) (1+ (cdar acc))) new-string))))
 input :initial-value (cons (cons nil 14) (substring input 0 14)) :start 14)
