
(defun letter-to-number (xyz)
  (cond ((string= xyz "X") 0)
	((string= xyz "Y") 1)
	((string= xyz "Z") 2)
	((string= xyz "A") 0)
	((string= xyz "B") 1)
	((string= xyz "C") 2)
	('t xyz)))

(defun parse-input (str)
  (mapcar (lambda (x) (mapcar #'letter-to-number (split-string x " ")))
	  (split-string str "\n")))

(defun calculate-score (round)  
  (let* ((enemy (car round))
	 (you (cadr round))
	 (difference (% (+ (- enemy you) 3) 3)))
    (+ (1+ you)
     (cond ((= difference 0) 3)
	   ((= difference 1) 0)
	   ((= difference 2) 6)))))

(let
    ((input (parse-input (f-read "input"))))
  (apply '+ (mapcar #'calculate-score input)))
