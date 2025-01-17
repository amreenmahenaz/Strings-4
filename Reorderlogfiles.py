class Solution:
    def reorderLogFiles(self, logs):
        digits = []
        letters = []
		# divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key = lambda x: x.split()[1])            #when suffix is tie, sort by identifier
		letters.sort(key = lambda x: x.split()[1:])           #sort by suffix
        result = letters + digits                                        #put digit logs after letter logs
        return result
