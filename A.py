def nextGreaterElement(nums1:list,nums2:list)->list:
    if len(nums1)==0 or len(nums2)==0:
        return []
    else:
        o=[]
        for i in range(len(nums1)):
            for k in range(len(nums2)):
                if nums2[k]==nums1[i]:
                    for j in range(k+1,len(nums2)):
                        if nums2[j]>nums1[i]:
                            o+=[nums2[j]]
                            break
                    else:
                        o+=[-1]
        return o
print(nextGreaterElement([4,1,2],[1,3,4,2]))