(defun is-valid-cargo-name(c)
  (and (>= c ?A) (<= c ?Z)))

(defun parse-cargo (cargo new-line)
  (dotimes (i (length new-line))
    (let ((c (aref new-line i))
	  (index (/ i 4)))
      (when (is-valid-cargo-name c)
	(setf (aref cargo index) (reverse (cons c (reverse (aref cargo index))))))))
  cargo)

(defun move-cargo (cargo command)
  (let ((n (car command))
	(from (1- (cadr command)))
	(to (1- (caddr command))))
    (setf
     (aref cargo to)
     (append (subseq (aref cargo from) 0 n) (aref cargo to)))
    (setf (aref cargo from) (nthcdr n (aref cargo from)))
    cargo))

(defun parse-command (str)
  (mapcar (lambda (x) (string-to-number x))
	  (let ((str (split-string str " ")))
	    (list (nth 1 str) (nth 3 str) (nth 5 str)))))

(defun parse-input (str)
  (reduce
   (lambda (acc x)
     (cond
      ((string-match-p "\\[" x)
       (cons
	(parse-cargo (car acc) x)
	(cdr acc)))
      ((string-match-p "move" x)
       (cons (car acc) (cons x (cdr acc))))
      ('t acc)))
   (split-string (string-chop-newline str) "\n")
   :initial-value (cons (vector nil nil nil nil nil nil nil nil nil) nil)))

(let* ((input (parse-input (f-read "input")))
       (parsed-commands
	(reverse (mapcar (lambda (x) (parse-command x))
		(cdr input)))))
  (mapcar (lambda (x)
	    (setcar input (move-cargo (car input) x)) nil)
	  parsed-commands)
  (apply #'string (mapcar (lambda (x) (car x)) (car input))))

